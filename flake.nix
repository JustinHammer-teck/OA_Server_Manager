{
  description = "A Nix-flake-based python development environment - this only fit with my Intel-base MacBook";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      ...
    }@inputs:
    flake-utils.lib.eachSystem [ "x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin" ] (
      system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
      in
      {

        devShells.default = pkgs.mkShell {
          name = "labelstudio";
          nativeBuildInputs =
            with pkgs;
            [
              python313
              ty
              uv
              ruff
              nodejs
              pnpm
            ]
            ++ (with pkgs.python313Packages; [
              python-lsp-server
              pylsp-rope
            ]);

          shellHook = ''
            # source .venv/bin/activate
          '';

          RUFFPATH = "${pkgs.ruff}/bin/ruff";
          TYPATH = "${pkgs.ty}/bin/ty";
          PYLSP = "${pkgs.python313Packages.python-lsp-server}/bin/pylsp";
        };
      }
    );
}
