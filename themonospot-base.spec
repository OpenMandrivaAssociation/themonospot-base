Summary: Base component for themonospot components
Name:    themonospot-base
Version: 0.8.2
Release: 2
License: GPLv2
Group:   Video
Source:  http://www.integrazioneweb.com/repository/SOURCES/themonospot-base-%{version}.tar.gz
Url:     https://www.integrazioneweb.com/themonospot

#BuildArch : noarch
%define debug_package %{nil}

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
Requires: %{name} = %{EVRD}


%description devel
Development files for themonospot-base 


%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
chmod 0755 %{buildroot}%{_libdir}/themonospot/*.dll

%files
%doc themonospot-base/readme themonospot-base/copying.gpl
%{_libdir}/themonospot/
%{_datadir}/themonospot/

%files devel
%{_libdir}/pkgconfig/* 
