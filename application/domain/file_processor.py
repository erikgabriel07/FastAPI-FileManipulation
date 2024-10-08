import os, csv, time
from fastapi.exceptions import HTTPException
from fastapi import status, UploadFile


class FileProcessor:
    """ File manager and folders processing. """

    def __init__(self) -> None:
        self.file_path = os.path.join('data', 'your_file.csv')
        self.directory = 'data'

    def create_file(self) -> HTTPException | object:
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

            with open(self.file_path, 'w' ,newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Conta', 'Agencia', 'Texto', 'Valor'])

                return {'message': f'O arquivo \'{self.file_path}\' foi criado com sucesso!'}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O arquivo já existe!")
    
    async def upload_file(self, file: UploadFile):
        """
        Upload a file to read and print its data.

        :param file: Uploaded file
        :return: Success or error
        """

        if file.content_type == 'text/csv':
            try:
                contents = await file.read()
                decoded_file = contents.decode('utf-8').splitlines()
                
                csv_reader = csv.DictReader(decoded_file)
                for row in csv_reader:
                    print(row)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail={'message': 'Erro ao processar arquivo!', 'error': str(e)})
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail={'message': 'Tipo de arquivo inválido! Apenas CSV permitido!'})
        return {'message': 'Seu arquivo foi processado com sucesso!'}

    async def add_data_to_file(self, data: dict):
        """
        Add data to a created file
        :param data: account data history
        :return: error or success message
        """

        if os.path.exists(self.file_path):
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([data['Conta'], data['Agencia'], data['Texto'], data['Valor']])
                return {'message': 'Dados adicionados com sucesso!', 'data': data}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail={'message': 'O arquivo indicado não existe! '
                                        'Por favor, acesse a rota para a criação do arquivo.'})
    
    async def delete_data(self, selected_line: int):
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='r') as file:
                lines = file.readlines()

            if selected_line < 1 or selected_line >= len(lines):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'message': 'Linha selecionada inválida!'})
            
            with open(self.file_path, mode='w') as file:
                for index, line in enumerate(lines):
                    if index != selected_line:
                        file.write(line)
            return {'message': 'Linha deletada com sucesso'}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'Arquivo não encontrado! '
                                                                               'Por favor, crie um arquivo.'})
        
    async def file_content_listing(self):
        """
        This function list all lines
        that a csv file contains
        :return: error message or dictionary
        """
        
        if os.path.exists(self.file_path):
            start_time = time.perf_counter()
            with open(self.file_path, mode='r') as file:
                data = dict()
                lines = file.readlines()
                headers = lines[0].split(',')
                for i, line in enumerate(lines[1:]):
                    line_values = line.split(',')
                    data[f'linha_{i+1}'] = {headers[0]: line_values[0],
                                            headers[1]: line_values[1],
                                            headers[2]: line_values[2],
                                            headers[3]: line_values[3],
                                            }
            end_time = time.perf_counter()
            exec_time = end_time - start_time
            return {'timing': f'{exec_time:.3f}s', 'data': data}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail={'message': 'O arquivo indicado não existe! '
                                        'Por favor, acesse a rota para a criação do arquivo.'})
