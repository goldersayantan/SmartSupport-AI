from src.database import SessionLocal, User
from src.auth import hash_password


db = SessionLocal()

try:
    # Check whether an admin already exists
    existing_admin = (
        db.query(User)
        .filter(User.role == "admin")
        .first()
    )

    if existing_admin:
        print("An admin account already exists.")
        print(f"Admin email: {existing_admin.email}")

    else:
        name = input("Enter admin name: ").strip()
        email = input("Enter admin email: ").strip()
        password = input("Enter admin password: ")

        # Check whether this email is already registered
        existing_user = (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

        if existing_user:
            print("This email is already registered.")
        else:
            admin = User(
                name=name,
                email=email,
                password_hash=hash_password(password),
                role="admin"
            )

            db.add(admin)
            db.commit()
            db.refresh(admin)

            print("Admin account created successfully.")
            print(f"Admin ID: {admin.id}")
            print(f"Admin email: {admin.email}")

finally:
    db.close()

