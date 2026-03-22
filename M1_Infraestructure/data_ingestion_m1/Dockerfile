FROM python:3.13-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:/mingw64/bin:/usr/bin:/c/Users/nesto/bin:/c/Users/nesto/AppData/Roaming/Code/User/globalStorage/github.copilot-chat/debugCommand:/c/Users/nesto/AppData/Roaming/Code/User/globalStorage/github.copilot-chat/copilotCli:/c/Users/nesto/AppData/Local/Programs/Microsoft VS Code 1.100.2:/c/Users/nesto/AppData/Local/Programs/Python/Python313/Scripts:/c/Users/nesto/AppData/Local/Programs/Python/Python313:/c/Program Files/Common Files/Oracle/Java/javapath:/c/WINDOWS/system32:/c/WINDOWS:/c/WINDOWS/System32/Wbem:/c/WINDOWS/System32/WindowsPowerShell/v1.0:/c/WINDOWS/System32/OpenSSH:/c/Program Files/dotnet:/cmd:/c/Program Files/nodejs22:/c/ProgramData/chocolatey/bin:/c/WINDOWS/system32/config/systemprofile/AppData/Local/Muse Hub/lib:/c/ApacheJmeter5.6.3/bin:/c/Program Files/Docker/Docker/resources/bin:/c/terraform:/c/Users/nesto/.bruin:/c/Users/nesto/AppData/Local/Programs/Python/Python312/Scripts:/c/Users/nesto/AppData/Local/Programs/Python/Python312:/c/Users/nesto/AppData/Local/Programs/Python/Python314/Scripts:/c/Users/nesto/AppData/Local/Programs/Python/Python314:/c/Users/nesto/.console-ninja/.bin:/c/Users/nesto/AppData/Local/Microsoft/WindowsApps:/c/Users/nesto/AppData/Local/Programs/Microsoft VS Code 1.100.2/bin:/c/Users/nesto/AppData/Local/Muse Hub/lib:/c/Users/nesto/AppData/Roaming/npm:/c/Users/nesto/Downloads/edgedriver_win64:/c/Users/nesto/AppData/Local/Google/Cloud SDK/google-cloud-sdk/bin:/c/Users/nesto/.vscode/extensions/ms-python.debugpy-2025.18.0-win32-x64/bundled/scripts/noConfigScripts:/c/Users/nesto/.console-ninja/.bin:/c/Users/nesto/.local/bin:/c/Users/nesto/.local/bin"

COPY pyproject.toml .python-version ./

RUN pip install pandas pyarrow sqlalchemy psycopg2-binary tqdm click

COPY scripts/ scripts/
COPY data/ data/

ENTRYPOINT ["python", "scripts/ingest_data.py"]
