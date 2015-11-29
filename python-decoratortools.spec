#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		module	DecoratorTools
Summary:	Use class and function decorators -- even in Python 2.3
Name:		python-decoratortools
Version:	1.8
Release:	2
License:	Python or ZPLv2.1
Group:		Development/Languages
URL:		http://pypi.python.org/pypi/DecoratorTools
Source0:	http://pypi.python.org/packages/source/D/DecoratorTools/%{module}-%{version}.zip
# Source0-md5:	f161004115c3d04ed976c230c8a91d87
BuildRequires:	python-devel
%{?with_tests:BuildRequires:	python-nose}
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-setuptools
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Want to use decorators, but still need to support Python 2.3? Wish you
could have class decorators, decorate arbitrary assignments, or match
decorated function signatures to their original functions? Then you
need "DecoratorTools".

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--root $RPM_BUILD_ROOT

%py_postclean

%if %{with tests}
PYTHONPATH=$(pwd) nosetests-%{py_ver} -q
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{py_sitescriptdir}/peak
%dir %{py_sitescriptdir}/peak/util
%{py_sitescriptdir}/peak/util/decorators.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py%{py_ver}.egg-info
%{py_sitescriptdir}/%{module}-%{version}-py%{py_ver}-nspkg.pth
