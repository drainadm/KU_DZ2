# test.py
from main import load_config, get_commit_dependencies, generate_mermaid_graph

def test_load_config():
    config = load_config('config.yaml')
    assert 'repository_path' in config
    assert 'output_file' in config

def test_get_commit_dependencies():
    # Убедитесь, что путь к репозиторию верный
    dependencies = get_commit_dependencies('C:/Users/drain/PycharmProjects/two/.git/')  # Укажите правильный путь к репозиторию
    assert isinstance(dependencies, dict)  # Проверяем, что результат - это словарь

def test_generate_mermaid_graph():
    dependencies = {
        'commit1': ['parent1'],
        'commit2': ['parent1', 'parent2'],
    }
    mermaid_code = generate_mermaid_graph(dependencies)
    assert 'graph TD;' in mermaid_code  # Проверяем, что в выводе содержится граф
    assert 'parent1 --> commit1;' in mermaid_code  # Проверяем пары

if __name__ == "__main__":
    test_load_config()
    test_get_commit_dependencies()
    test_generate_mermaid_graph()
    print("All tests passed!")