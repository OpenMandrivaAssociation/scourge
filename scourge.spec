Summary:	Scourge is a roguelike game with a 3D user interface
Name:		scourge
Version:	0.19
Release:	%mkrel 1
License:	GPL
Group:		Games/Adventure
Url:		http://scourge.sourceforge.net/
Source0:	http://downloads.sourceforge.net/scourge/%{name}-%{version}.src.tar.bz2
BuildRequires:	mesa-common-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
Requires:	%{name}-data

%description
S.C.O.U.R.G.E. is a roguelike game with a 3D user interface.
The game allows a group of four characters to search for treasure, 
kill enemies, gain levels, etc.

%prep
%setup -qn %{name}

%build
autoreconf -i

%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir} \
	--with-data-dir=%{_gamesdatadir}/%{name} \
	--disable-rpath \
	--enable-optimized \
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

%post
%{update_menus}

%postun
%{clean_menus}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS README ChangeLog
%{_gamesbindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
