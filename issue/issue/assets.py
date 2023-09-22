from dagster import asset
@asset()
def anAsset() :
    aList = [1,2,3,4,5,5,5]
    return aList

