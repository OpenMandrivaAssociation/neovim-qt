Name: neovim-qt
Version:	0.2.17
Release:	2
# 
Source0: https://github.com/equalsraf/neovim-qt/archive/v%{version}/%{name}-%{version}.tar.gz
Summary: Qt frontend for the neovim editor
URL: https://github.com/equalsraf/neovim-qt
License: GPL
Group: Editors
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: pkgconfig(termkey)
BuildRequires: pkgconfig(unibilium)
BuildRequires: pkgconfig(vterm)
BuildRequires: pkgconfig(libluv)
BuildRequires: cmake(msgpack)
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: neovim
BuildRequires: qt5-macros
BuildRequires: qmake5
Requires: neovim

%description
Qt frontend for the neovim editor

%prep
%autosetup -p1
%cmake_qt5 \
	-DUSE_SYSTEM_MSGPACK:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/nvim-qt
%{_datadir}/icons/hicolor/*/apps/nvim-qt.*
