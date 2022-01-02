pragma solidity 0.8.10;

contract election {
	uint[2] private votes;
	mapping(address => bool) public voters;
	
	constructor() public {
		votes[0]=0;
		votes[1]=0;
	}

	function castVote(uint id) public {
		
		require(!voters[msg.sender]);
		voters[msg.sender]=true;
		
		if(id==0) {
			votes[0]+=1;
		} else if(id==1) {
			votes[1]+=1;
		}
	}

	function viewVote() public view returns(uint[2] memory) {
		return(votes);
	}
}