# Full Api GraphQL

mutation MyM {
  __typename
  addUser(name: "Javi"){
    ...on AddUser {
			id
      name
}
		...on UserExists {
			message
	}
}
	addStickynotes(text: "demo text", userId: 1) {
		...on StickyNotes {
			id 
      text
  }
}
}