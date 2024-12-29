{ pkgs? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.11") {} }:

pkgs.mkShellNoCC {
  packages = with pkgs; [
    pre-commit

    python3

    go

    cargo
    rustc
  ];

  shellHook = ''
    pre-commit install
  '';
}
