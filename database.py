import sqlite3




def save_user(data):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO clients (user_id,
            full_name, phone_number,
            about_project, active_time,
            income, partner, need_invest,
            spend, return_time, multiply_income,
            privilege_time, can_suggest, is_accept)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data['user_id'], data['full_name'], data['phone_number'],
                data['about_project'], data['active_time'], data['income'],
                data['partner'], data['need_invest'], data['spend'],
                data['return_time'], data['multiply_income'], data['privilege_time'],
                data['can_suggest'], data['is_accept']
            ))

        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False






