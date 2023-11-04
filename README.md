# choreo-testing

curl -X POST http://localhost:5000/checkout -H "Content-Type: application/json" -d '{"book_id": 1}'
# choreo-testing

curl -X POST http://localhost:5000/checkin -H "Content-Type: application/json" -d '{"book_id": 1}'


FAQ - connect reset error means backend service is not started, port is wrong, or it is not accesible outside 


dev docs - https://docs.dv.choreo.dev/choreo/docs/develop-components/deploy-an-application-with-buildpacks/ 


go mod init my-go-service


