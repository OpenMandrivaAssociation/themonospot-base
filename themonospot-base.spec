Summary   : Base component for themonospot system, parser/editor and content descriptor
Name      : themonospot-base
Version   : 0.8.1
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-base-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono >= 1.2.3
BuildRequires: pkgconfig

Requires: mono >= 1.2.3

# Suggest principal plugins
Suggests: themonospot-plugin-avi
Suggests: themonospot-plugin-mkv

%description
themonospot-base is core package for themonospot system. It install:
    - themonospot-base mono assembly in GAC (use from other gui applications)
    - themonospot-plugin-interface in GAC (use to write plugins)
    - themonospot-plugin-manager (use to load plugins at runtime)
    - xml language files


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc themonospot-base/readme themonospot-base/copying.gpl
%{_libdir}/%{name}/
%{_libdir}/mono/
%{_libdir}/pkgconfig/themonospot-base.pc
%{_libdir}/pkgconfig/themonospot-plugin-interface.pc
%{_datadir}/themonospot/

%changelog
* Mon Dec 14 2009 Armando Basile <hmandevteam@gmail.com> 0.8.1-1mdv2010.1
- first release of new base component

