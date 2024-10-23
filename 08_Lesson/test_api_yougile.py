import pytest

from Auth_YouGile import Auth_YouGile
from Projects_YouGile import Projects_YouGile

api = Auth_YouGile("https://ru.yougile.com/api-v2")
pro = Projects_YouGile("https://ru.yougile.com/api-v2")


@pytest.mark.positive_test
def test_add_new_project():

    project_list_before = pro.list_of_projects()
    result_before = project_list_before['paging']['count']

    pro.new_project('Api in Python')

    project_list_after = pro.list_of_projects()
    result_after = project_list_after['paging']['count']

    assert result_after - result_before == 1


@pytest.mark.positive_test
def test_get_list_of_project():

    title_of_new_project = 'My 8 homework'
    pro.new_project(title_of_new_project)
    info = pro.list_of_projects()

    assert info['content'][-1]['title'] == title_of_new_project


@pytest.mark.positive_test
def test_delete_project():

    project_list_before = pro.list_of_projects()
    result_before = project_list_before['paging']['count']

    title_of_new_project = 'Создадим и удалим'
    project = pro.new_project(title_of_new_project)
    id_project = project['id']

    project_list_after = pro.list_of_projects()
    result_after = project_list_after['paging']['count']

    pro.change_project(id_project, title_of_new_project)

    list_after_deletion = pro.list_of_projects()
    result_after_deletion = list_after_deletion['paging']['count']

    assert result_after - result_before == 1
    assert result_before == result_after_deletion


@pytest.mark.positive_test
def test_get_project_by_id():

    title_of_new_project = 'Очередной проект'
    project = pro.new_project(title_of_new_project)
    id_project = project['id']

    project_info = pro.get_project(id_project)

    assert project_info['id'] == id_project
    assert project_info['title'] == title_of_new_project


@pytest.mark.negative_test
def test_add_project_with_empty_title():

    project_list_before = pro.list_of_projects()
    result_before = project_list_before['paging']['count']

    project_title = ''
    pro.new_project(project_title)

    project_list_after = pro.list_of_projects()
    result_after = project_list_after['paging']['count']

    assert result_after == result_before
