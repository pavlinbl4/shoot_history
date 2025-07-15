def make_page_link(shoot_id):
    shoot = shoot_id.split('_')
    return f"https://image.kommersant.ru/photo/wp/default.aspx?shootnum={shoot[1]}&sourcecode={shoot[0]}"


def make_history_link(inner_id:str):
    return f'https://image.kommersant.ru/photo/archive/adm/ShootHistoryLog.aspx?id={inner_id}&insid=-{inner_id}'


def get_inner_id(shoot_history_link:str):
    return shoot_history_link.split('=')[1]
