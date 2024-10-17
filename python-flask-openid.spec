%global mod_name Flask-OpenID

Name:		python-flask-openid
Version:	1.2.1
Release:	4
Summary:	OpenID support for Flask


Group:		Development/Python
License:	BSD
URL:		https://github.com/mitsuhiko/flask-openid/
Source0:	http://pypi.python.org/packages/source/F/Flask-OpenID/Flask-OpenID-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-flask
BuildRequires:	python-openid
BuildRequires:	python-setuptools

BuildRequires:  python2-devel
BuildRequires:  python2-flask
BuildRequires:  python2-openid
BuildRequires:  python2-setuptools

Requires:	python-openid

%description
Flask-OpenID is an extension to flask that allows you to add openid
based authentication to your website in a matter of minutes.

%package -n python2-flask-openid

%prep
%setup -q -n %{mod_name}-%{version}
rm -f docs/.DS_Store
rm -f docs/_static/.DS_Store
rm -f docs/_static/._.DS_Store
rm -f docs/._.DS_Store

cp -a . %py2dir

%build
CFLAGS="%{optflags}" python setup.py build

pushd %py2dir
CFLAGS="%{optflags}" python2 setup.py build


%install
python setup.py install -O1 --skip-build --root %{buildroot}

pushd %py2dir
python2 setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc docs LICENSE PKG-INFO README
%{py_puresitedir}/*.egg-info/
%{py_puresitedir}/flask_openid.py

%files -n python2-flask-openid
%doc docs LICENSE PKG-INFO README
%{py2_puresitedir}/*.egg-info/
%{py2_puresitedir}/flask_openid.py


