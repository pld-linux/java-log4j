Summary: 	log4j
Summary(pl):	log4j
Name:		jakarta-log4j
Version:	1.1.3
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	http://jakarta.apache.org/%{name}/%{name}-%{version}.tar.gz
URL:		http://jakarta.apache.org
Requires:	javamail
Requires:	jms
Requires:	junit
Requires:	xerces-j
Requires:	ibm-java-sdk
BuildRequires:	javamail
BuildRequires:	jms
BuildRequires:	junit
BuildRequires:	xerces-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
log4j

%package doc
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Summary: 	Online manual for log4j

%description doc
Online manual for log4j

%prep
%setup -q

%build
export JAVA_HOME="/usr/lib/IBMJava2-13"
export CLASSPATH="$CLASSPATH:$JAVA_HOME/jre/lib/rt.jar"
export CLASSPATH="$CLASSPATH:%{_javalibdir}/mail.jar"
export CLASSPATH="$CLASSPATH:%{_javalibdir}/jms.jar"
export CLASSPATH="$CLASSPATH:%{_javalibdir}/activation.jar"
export CLASSPATH="$CLASSPATH:%{_javalibdir}/junit.jar"
export CLASSPATH="$CLASSPATH:%{_javalibdir}/classes/xerces.jar"

sh build.sh jar
sh build.sh javadoc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_javalibdir}
cp dist/lib/*.jar $RPM_BUILD_ROOT/%{_javalibdir}

gzip -9nf LICENSE.APL

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javalibdir}/*.jar

%files doc
%defattr(644 root root 755)
%doc docs/*
