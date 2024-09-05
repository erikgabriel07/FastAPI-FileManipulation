import os
import csv
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
                csv_reader = csv.DictReader(file.file)
                for row in csv_reader:
                    data = {'conta': row[0], 'agencia': row[1], 'texto': row[2], 'valor': float(row[3])}
                print(data)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail={'message': 'Erro ao processar arquivo!', 'error': str(e)})
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail={'message': 'Tipo de arquivo inválido! Apenas CSV permitido!'})