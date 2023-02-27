docker-build:
	docker build -t test-application application

docker-run-local-test:
	docker run -it --rm -p 8080:80 test-application

docker-save:
	mkdir build
	docker save -o build/test-application-docker-export.tar test-application

clean:
	rm -rf build
	docker rmi test-application
