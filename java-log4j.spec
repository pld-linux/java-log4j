Summary:	log4j - logging for Java
Summary(pl):	log4j - zapis log�w dla Javy
Name:		jakarta-log4j
Version:	1.2.6
Release:	2
License:	Apache
Group:		Development/Languages/Java
Source0:	http://jakarta.apache.org/log4j/%{name}-%{version}.tar.gz
# Source0-md5:	847a4624f29af8c902a6161c3c69b794
Patch0:		%{name}-unreachable.patch
URL:		http://jakarta.apache.org/
BuildRequires:	jakarta-ant
BuildRequires:	javamail >= 1.2
BuildRequires:	jdk >= 1.2
BuildRequires:	jms
BuildRequires:	junit >= 3.8
BuildRequires:	xerces-j
Requires:	javamail >= 1.2
Requires:	jdk >= 1.2
Requires:	jms
Requires:	junit
Requires:	xerces-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

%description
With log4j it is possible to enable logging at runtime without
modifying the application binary.

%description -l pl
Przy u�yciu log4j mo�na w��czy� zapis do log�w przy uruchamianiu bez
modyfikowania binarnej aplikacji.

%package doc
Summary:	Online manual for log4j
Summary(pl):	Dokumentacja online do log4j
Group:		Development/Languages/Java

%description doc
Online manual for log4j.

%description doc -l pl
Dokumentacja online do log4j.

%prep
%setup -q
%patch -p1

%build
JAVA_HOME="/usr/lib/java"
CLASSPATH="$CLASSPATH:$JAVA_HOME/jre/lib/rt.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/mail.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/jms.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/activation.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/junit.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/classes/xerces.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/jmxri.jar"
CLASSPATH="$CLASSPATH:%{_javalibdir}/jmxtools.jar"
export JAVA_HOME CLASSPATH

ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
install dist/lib/log4j-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf log4j-%{version}.jar $RPM_BUILD_ROOT%{_javalibdir}/log4j.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javalibdir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*
