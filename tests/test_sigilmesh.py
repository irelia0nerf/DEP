from src.sigilmesh import mint_reputation_nft


def test_mint_reputation_nft():
    nft = mint_reputation_nft({"wallet": "0xabc"})
    assert nft["nft_id"] == "nft-0xabc"
    assert nft["analysis"]["wallet"] == "0xabc"
