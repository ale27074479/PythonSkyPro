import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from database import DATABASE_URL


@pytest.fixture
def db_session():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    # Очистка таблицы после теста
    session.query(Student).delete()
    session.commit()
    session.close()


def test_create_student(db_session):
    """Тест на создание студента."""
    new_student = Student(name="Test User", email="test@example.com")
    db_session.add(new_student)
    db_session.commit()

    student = db_session.query(Student).filter_by(email="test@example.com").first()
    assert student is not None
    assert student.name == "Test User"


def test_update_student(db_session):
    """Тест на обновление данных студента."""
    # Сначала создаем студента
    student = Student(name="Update Test", email="update@test.com")
    db_session.add(student)
    db_session.commit()

    # Обновляем данные
    student.name = "Updated Name"
    db_session.commit()

    # Проверяем обновление
    updated_student = db_session.query(Student).filter_by(
        email="update@test.com"
    ).first()
    assert updated_student.name == "Updated Name"


def test_soft_delete_student(db_session):
    """Тест на мягкое удаление студента."""
    # Создаем студента
    student = Student(name="Delete Test", email="delete@test.com")
    db_session.add(student)
    db_session.commit()

    # Soft delete
    student.is_active = False
    db_session.commit()

    # Проверяем, что студент "удален"
    deleted_student = db_session.query(Student).filter_by(
        email="delete@test.com"
    ).first()
    assert deleted_student.is_active is False

    # Проверяем, что студент все еще в БД
    assert db_session.query(Student).filter_by(email="delete@test.com").count() == 1
    