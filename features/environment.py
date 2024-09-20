import allure
import platform
import os
import importlib.metadata


def get_system_info():
    """Retrieve system information such as OS, release, version, and Python version."""
    return {
        "os_platform": platform.system().lower(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "python_version": f"Python {platform.python_version()}"
    }


def get_required_packages(requirements_file):
    """Read libraries from the requirements.txt file."""
    if not os.path.exists(requirements_file):
        raise FileNotFoundError(f"'{requirements_file}' not found.")

    with open(requirements_file, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def get_installed_packages(required_packages):
    """Retrieve the versions of installed packages from requirements.txt."""
    installed_packages = {pkg.metadata['Name']: pkg.version for pkg in importlib.metadata.distributions()}
    return {pkg: installed_packages.get(pkg.lower(), "not installed") for pkg in required_packages}


def write_environment_properties(file_path, system_info, matching_packages):
    """Write system information and library versions to environment.properties file."""
    with open(file_path, 'w') as file:
        # Write system information
        for key, value in system_info.items():
            file.write(f"{key}={value}\n")

        file.write("\n# Installed libraries based on requirements.txt\n")
        # Write library information
        for pkg, version in matching_packages.items():
            file.write(f"{pkg}={version}\n")


def generate_environment_file(requirements_file="requirements.txt", output_dir="allure-results"):
    """Main function to generate the environment.properties file."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Directory '{output_dir}' created.")
    else:
        print(f"Directory '{output_dir}' already exists.")

    system_info = get_system_info()
    required_packages = get_required_packages(requirements_file)
    matching_packages = get_installed_packages(required_packages)


    properties_file_path = os.path.join(output_dir, "environment.properties")
    write_environment_properties(properties_file_path, system_info, matching_packages)
    print(f"'environment.properties' successfully created in '{output_dir}'.")


def before_all(context):
    """Hook that runs before all tests to generate the environment file once."""
    output_dir = "allure-results"

    if not os.path.exists(os.path.join(output_dir, "environment.properties")):
        print("Generating environment file before tests...")
        generate_environment_file(requirements_file="requirements.txt", output_dir=output_dir)
    else:
        print("Environment file already exists, skipping generation.")



if __name__ == "__main__":
    try:
        generate_environment_file()
    except Exception as e:
        print(f"Error: {e}")
