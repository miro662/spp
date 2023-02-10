import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__, specification_dir="./api/docs")
app.add_api("swagger.yml", resolver=RestyResolver("spp.api"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
