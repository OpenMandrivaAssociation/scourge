Summary:	Scourge is a roguelike game with a 3D user interface
Name:		scourge
Version:	0.18
Release:	%mkrel 1
License:	GPL
Group:		Games
Url:		http://scourge.sourceforge.net/
Source0:	http://downloads.sourceforge.net/scourge/%{name}-%{version}.src.tar.bz2
Source1:	http://downloads.sourceforge.net/scourge/%{name}-%{version}.data.tar.bz2
BuildRequires:	mesa-common-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	desktop-file-utils
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
S.C.O.U.R.G.E. is a roguelike game with a 3D user interface.
The game allows a group of four characters to search for treasure, 
kill enemies, gain levels, etc.

%prep
%setup -qn %{name} -a 1

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
install -d %{buildroot}%{_gamesdatadir}/%{name}
install -d %{buildroot}{%{_datadir}/applications,%{_datadir}/pixmaps}
cp -rf %{name}_data/* %{buildroot}%{_gamesdatadir}/%{name}
install assets/%{name}.desktop %{buildroot}%{_datadir}/applications
install assets/%{name}.png %{buildroot}%{_datadir}/pixmaps

desktop-file-install --vendor="" \
	    --add-category="X-MandrivaLinux-MoreApplications-Games-Adventure;" \
	    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
