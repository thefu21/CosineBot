{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.setuptools
    pkgs.python311Packages.virtualenv
    pkgs.ffmpeg
  ];

  # Optional: Wenn du auto-aktivierung willst mit direnv + nix-direnv
  shellHook = ''
    echo "🔧 Setting up Python virtual environment..."
    if [ ! -d .venv ]; then
      python -m venv .venv
    fi
    source .venv/bin/activate

    # Installiere Abhängigkeiten nur, wenn requirements.txt vorhanden ist
    if [ -f requirements.txt ]; then
      echo "📦 Installing requirements..."
      pip install -r requirements.txt
    fi

    export PATH=$PATH:${pkgs.ffmpeg}/bin

    echo "✅ Virtualenv aktiv & bereit!"
  '';
}
