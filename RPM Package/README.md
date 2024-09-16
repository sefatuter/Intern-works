# Create RPM Package in CentOS 8

To Create RPM setup tree ```rpmdev-setuptree```
Then ```cd SPECS/```
```
rpmbuild -ba netflow2ng.spec
rpmbuild -ba msmtp.spec
```

```
go clean -cache

mkdir -p dist/

go build -ldflags='-X "main.Version=0.0.5" -X "main.Delta=1750" -X "main.Buildinfos=2024-08-12T02:08:57-0400" -X "main.Tag=v0.0.5-1-g52df391" -X "main.CommitID=52df39156d3e3796cb54f270dc07e86868c8e211"' -o dist/netflow2ng-0.0.5 ./cmd/...
```

``` netflow2ng -h``` to check netflow

```tar -czvf ~/rpmbuild/SOURCES/netflow2ng-x.y.z.tar.gz ./netflow2ng/``` Create Tar

```git clone https://github.com/synfinatic/netflow2ng.git```

if libidn-devel not works -> ```sudo dnf install zeromq-devel```

Go Setup
```
wget https://golang.org/dl/go1.19.5.linux-amd64.tar.gz 

sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.19.5.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
```
