from model import app
from tests.test_data.users import user, Subject, Hobby


def test_submit_student_registration_form():
    (
        app.registration_form.given_opened()

        .set_first_name(user.name)
        .set_last_name(user.last_name)
        .set_email(user.email)
        .set_gender(user.gender)
        .set_user_number(user.user_number)
        .set_date_of_birthday(user.date)
        .add_subjects(user.subjects)
        .select_hobbies_cb(user.hobbies)
        .upload_picture(user.picture_file)
        .set_current_address(user.current_address)
        .scroll_to_bottom()
        .set_state(user.state)
        .set_city(user.city)
        .submit_form()



        .should_have_submitted(
            [
                ('Student Name', f'{user.name} {user.last_name}'),
                ('Student Email', user.email),
                ('Gender', user.gender),
                ('Mobile', user.user_number),
                ('Date of Birth', '10 October,1984'),
                ('Subjects', Subject.History.value),
                ('Hobbies', Hobby.Sports.name),
                ('Picture', user.picture_file),
                ('Address', user.current_address),
                ('State and City', f'{user.state} {user.city}')
            ],
        )
    )
