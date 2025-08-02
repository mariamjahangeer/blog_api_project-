from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,database
router= APIRouter(
    prefix="/comments",
    tags=["comments"]
)
# create a comment
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.CommentOut)
def create_comment(comment:schemas.CommentBase,db:Session=Depends(database.get_db)):
    new_comment= models.comment(**comment.dict())
    db.add(new_comment)
    db.commit()
    return new_comment
