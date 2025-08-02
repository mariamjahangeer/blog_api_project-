from fastapi import APIROUTER,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .. import models,schemas,database
router= APIROUTER(
    prefix="/comments",
    tags=["comments"]
)
# create a comment
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Commentout)
def create_comment(comment:schemas.Commentcreate,db:Session=Depends(database.get_db)):
    new_comment= models.comment(**comment.dict())
    db.add(new_comment)
    db.commit()
    return new_comment
