%define git 20230907

Name: neovim-qt
Version:	0.2.18
Release:	%{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://github.com/equalsraf/neovim-qt/archive/refs/heads/master.tar.gz
%else
Source0: https://github.com/equalsraf/neovim-qt/archive/v%{version}/%{name}-%{version}.tar.gz
%endif
Summary: Qt frontend for the neovim editor
URL: https://github.com/equalsraf/neovim-qt
License: GPL
Group: Editors
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(termkey)
BuildRequires: pkgconfig(unibilium)
BuildRequires: pkgconfig(vterm)
BuildRequires: pkgconfig(libluv)
BuildRequires: cmake(msgpack-c)
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: neovim
Requires: neovim

%description
Qt frontend for the neovim editor

%prep
%autosetup -p1 -n %{name}-%{?git:master}%{!?git:%{version}}
%cmake \
	-DWITH_QT=Qt6 \
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
