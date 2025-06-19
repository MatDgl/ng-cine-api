from sqlmodel import SQLModel, Session, create_engine

# Remplace les identifiants ci-dessous avec les tiens
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/ngcine"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
