Summary:	Roguelike game with a 3D user interface
Name:		scourge
Version:	0.21.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Games/Adventure
Url:		https://scourgeweb.org/
Source0:	http://downloads.sourceforge.net/scourge/%{name}-%{version}.src.tar.lzma
Patch0:		scourge-0.21.1-fix-desktop-file.patch
BuildRequires:	mesa-common-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_net-devel
Requires:	%{name}-data = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
S.C.O.U.R.G.E. is a roguelike game with a 3D user interface.
The game allows a group of four characters to search for treasure, 
kill enemies, gain levels, etc.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir} \
	--with-data-dir=%{_gamesdatadir}/%{name} \
	--disable-rpath \
	--enable-optimized \
	--enable-threads=pth \
	--enable-stencil-buffer

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}{%{_datadir}/applications,%{_datadir}/pixmaps}
install assets/%{name}.desktop %{buildroot}%{_datadir}/applications
install assets/%{name}.png %{buildroot}%{_datadir}/pixmaps

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%{_gamesbindir}/%{name}
%attr(644,root,root) %{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
