from database.database import Database


async def initialize_database():
    db = Database(db_path='db.sqlite')
    await db.connect()
    await db.create_tables()
    return db
