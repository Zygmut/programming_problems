{ pkgs? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-24.05") {} }:

pkgs.mkShellNoCC {
  packages = with pkgs; [
    just
    pre-commit
    python3
  ];

  shellHook = ''
    pre-commit install
  '';
}
