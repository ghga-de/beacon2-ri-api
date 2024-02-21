from pymongo.mongo_client import MongoClient
import conf


client = MongoClient(
        "mongodb://{}:{}@{}:{}/{}?authSource={}".format(
            conf.database_user,
            conf.database_password,
            conf.database_host,
            conf.database_port,
            conf.database_name,
            conf.database_auth_source,
        )
    )


client.beacon.analyses.create_index([("$**", "text")])
client.beacon.biosamples.create_index([("$**", "text")])
client.beacon.cohorts.create_index([("$**", "text")])
client.beacon.datasets.create_index([("$**", "text")])
client.beacon.genomicVariations.create_index([("$**", "text")])
client.beacon.genomicVariations.create_index([("caseLevelData.biosampleId", 1)])
client.beacon.genomicVariations.create_index([("variation.location.interval.end.value", -1), ("variation.location.interval.start.value", 1)])
client.beacon.genomicVariations.create_index([("variantInternalId", 1), ("caseLevelData.biosampleId", 1)])
client.beacon.individuals.create_index([("$**", "text")])
client.beacon.runs.create_index([("$**", "text")])
#collection_name = client.beacon.analyses
#print(collection_name.index_information())

