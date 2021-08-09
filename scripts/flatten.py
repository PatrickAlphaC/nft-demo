from brownie import AdvancedCollectible


def main():
    flatten()


def flatten():
    file = open("./AdvancedCollectible_flattened.sol", "w")
    verification_information = AdvancedCollectible.get_verification_info()
    flattened_code = (
        verification_information["flattened_source"]
        .replace("\\n", "\n")
        .replace('\\"', '"')
    )
    file.write(flattened_code)
    file.close()
