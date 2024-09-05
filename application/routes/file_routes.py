from fastapi import (
    APIRouter, UploadFile, File
)
#from fastapi.exceptions import HTTPException
from domain.file_processor import FileProcessor


router = APIRouter()


@router.post('/file/create_file')
async def create_file():
    return FileProcessor().create_file()


@router.post('/file/upload_data')
async def upload_data(file: UploadFile = File()):
    return await FileProcessor().upload_file(file)


@router.delete('/file/delete_data')
async def delete_data():
    return {'message': 'Dados removidos com sucesso'}


@router.get('/file/list_files')
async def list_files():
    return {'message': 'Lista de dados'}