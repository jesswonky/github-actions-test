build-docker:
	docker build -t test-application:1.0.0 application

run-local-docker-test:
	docker run -it --rm -p 8080:80 test-application:1.0.0

clean:
	docker rmi test-application:1.0.0
