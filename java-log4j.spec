Summary: 	log4j - logging for Java
Summary(pl):	log4j - zapis logów dla Javy
Name:		jakarta-log4j
Version:	1.1.3
Release:	1
License:	Apache Software License
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Source0:	http://jakarta.apache.org/%{name}/%{name}-%{version}.tar.gz
URL:		http://jakarta.apache.org/
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
With log4j it is possible to enable logging at runtime without
modifying the application binary.

%description -l pl
Przy u¿yciu log4j mo¿na w³±czyæ zapis do logów przy uruchamianiu bez
modyfikowania binarnej aplikacji.

%package doc
Summary: 	Online manual for log4j
Summary(pl):	Dokumentacja online do log4j
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java

%description doc
Online manual for log4j.

%description doc -l pl
Dokumentacja online do log4j.

%prep
%setup -q

%build
JAVA_HOME="/usr/lib/IBMJava2-13"
CLASSPATH="$CLASSPATH:$JAVA_HOME/jre/lib/rt.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/mail.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/jms.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/activation.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/junit.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/classes/xerces.jar"
export JAVA_HOME CLASSPATH

sh build.sh jar
sh build.sh javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

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
