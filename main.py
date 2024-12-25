import os
import subprocess
import yaml


def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


def get_commit_dependencies(repo_path):
    os.chdir(repo_path)
    # Получаем коммиты и их родительские коммиты
    commits = subprocess.check_output(
        ["git", "log", "--pretty=format:%H %P"], text=True
    ).strip().split('\n')

    dependencies = {}
    for commit in commits:
        parts = commit.split()
        commit_hash = parts[0]
        parent_hashes = parts[1:]

        dependencies[commit_hash] = parent_hashes

    return dependencies


def generate_mermaid_graph(dependencies):
    mermaid_code = "graph TD;\n"
    for commit, parents in dependencies.items():
        for parent in parents:
            mermaid_code += f"    {parent} --> {commit};\n"
    return mermaid_code


def main(config_path):
    config = load_config(config_path)
    repo_path = config['repository_path']
    output_file = config['output_file']

    dependencies = get_commit_dependencies(repo_path)
    mermaid_code = generate_mermaid_graph(dependencies)

    with open(output_file, 'w') as file:
        file.write(mermaid_code)

    print(f"Generated Mermaid graph code in {output_file}")


if __name__ == "__main__":
    main('config.yaml')