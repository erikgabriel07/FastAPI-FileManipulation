from fastapi import APIRouter

router = APIRouter()


@router.post('/file/create_file')
async def create_file():
    return {'message': 'Arquivo criado com sucesso'}


@router.post('/file/add_data')
async def add_data():
    return {'message': 'Dados adicionados com sucesso'}


@router.delete('/file/delete_data')
async def delete_data():
    return {'message': 'Dados removidos com sucesso'}
