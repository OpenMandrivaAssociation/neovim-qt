Name: neovim-qt
Version: 0.2.0
Release: 1
# 
Source0: https://github.com/equalsraf/neovim-qt/archive/v0.2.0.zip 
Summary: Qt frontend for the neovim editor
URL: https://github.com/equalsraf/neovim-qt
License: GPL
Group: Editors
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: pkgconfig(termkey)
BuildRequires: pkgconfig(unibilium)
BuildRequires: pkgconfig(vterm)
BuildRequires: cmake
BuildRequires: ninja

%description
Qt frontend for the neovim editor

%prep
%setup
%cmake_qt5 \
	-DUSE_SYSTEM_MSGPACK:BOOL=ON \
	-G Ninja

%build
ninja -C build

%install
%ninja_install -C build

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/nvim-qt
%{_datadir}/pixmaps/nvim-qt.*
