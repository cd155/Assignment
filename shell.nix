{ pkgs ? import <nixpkgs> {} }:
let
  my-python-packages = ps: with ps; [
    #python packages
    django
    requests
    gunicorn
  ];
  my-python = pkgs.python3.withPackages my-python-packages;
in my-python.env