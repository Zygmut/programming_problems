{ pkgs? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05") {} }:

pkgs.mkShellNoCC {
  packages = with pkgs; [
    pre-commit

    python3
    go
  ];

  shellHook = ''
    pre-commit install
  '';
}
