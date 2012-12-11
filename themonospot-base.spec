Summary   : Base component for themonospot gui's/console components, parser/editor and content descriptor
Name      : themonospot-base
Version   : 0.8.2
Release   : %mkrel 1
License   : GPLv2
Group     : Video
Source    : http://www.integrazioneweb.com/repository/SOURCES/themonospot-base-%{version}.tar.gz
BuildRoot : %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL       : http://www.integrazioneweb.com/themonospot

#BuildArch : noarch

BuildRequires: mono-devel

Obsoletes: themonospot < 0.8.0

# Suggest principal plugins
Suggests: themonospot-plugin-avi > 0.1.0
Suggests: themonospot-plugin-mkv > 0.1.0

%description
themonospot-base is core package of themonospot suite. It install:
    - themonospot-base mono assembly (use from other gui applications)
    - themonospot-plugin-interface (use to write plugins)
    - themonospot-plugin-manager (use to load plugins at runtime)
    - xml language files


%package devel
Summary: Development files for themonospot-base
Group: Development/Other
Requires: %{name} = %{version}-%{release}


%description devel
Development files for themonospot-base 


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
%makeinstall_std
chmod 0755 %{buildroot}%{_libdir}/themonospot/*.dll


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc themonospot-base/readme themonospot-base/copying.gpl
%{_libdir}/themonospot/
%{_datadir}/themonospot/

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/* 





%changelog
* Sat Jan 02 2010 Armando Basile <hman@mandriva.org> 0.8.2-1mdv2010.1
+ Revision: 485098
- changed file permissions for dll assembly after buildroot install
- added Obsoletes
- removed GAC use

* Thu Dec 24 2009 Armando Basile <hman@mandriva.org> 0.8.1-1mdv2010.1
+ Revision: 481978
- update spec file Group
- first public release of core component of new Themonospot suite
- create themonospot-base

