%global mod_name Flask-OpenID

Name:		python-flask-openid
Version:	1.0.1
Release:	2
Summary:	OpenID support for Flask

Group:		Development/Python
License:	BSD
URL:		http://github.com/mitsuhiko/flask-openid/
Source0:	http://pypi.python.org/packages/source/F/%{mod_name}/%{mod_name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-flask
BuildRequires:	python-openid
BuildRequires:	python-setuptools
Requires:	python-openid

%description
Flask-OpenID is an extension to flask that allows you to add openid
based authentication to your website in a matter of minutes.

%prep
%setup -q -n %{mod_name}-%{version}
rm -f docs/.DS_Store
rm -f docs/_static/.DS_Store
rm -f docs/_static/._.DS_Store
rm -f docs/._.DS_Store

%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%files
%doc docs LICENSE PKG-INFO README
%{python_sitelib}/*-nspkg.pth
%{python_sitelib}/*.egg-info/
%{python_sitelib}/flaskext/*.py*
