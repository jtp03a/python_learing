{ pkgs }: {
<<<<<<< HEAD
	deps = [
		pkgs.python38Full
	];
  env = {
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
=======
  deps = [
    pkgs.python38Full
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      # Needed for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
      # Needed for matplotlib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
>>>>>>> d0fefe095dc3a344d5b8846fe016460f17c28a1b
  };
}