const MAX_LEN = 19
const WORD_MARKER = 'full_word'

export const appendingDFS = (str_so_far, tree, lst ) => {
  /*
  Depth first searches while appending to toAppend
  */
  // console.log(tree)
  // console.log(Object.entries(tree))
  if (tree.hasOwnProperty(WORD_MARKER))
  	lst.push(str_so_far)

  const keys = Object.getOwnPropertyNames(tree)
  for (var i = 0; i < keys.length; i++) {
  	let entry = keys[i]
  	if(entry === WORD_MARKER) {continue}
  	else {
  		appendingDFS(str_so_far+entry, tree[entry], lst)
  	}

  }
}

class Trie {
	constructor(serialized_trie) {
		this._trie = serialized_trie

	}

	query(word) {
		/*
		Checks if the Trie contains a word
		*/
		let ptr = {...this._trie}
		let tup = this._isSubstr(ptr, word)
		let i = tup[1]
		ptr = tup[0]
		if (i === MAX_LEN ) {
			let substr = word.slice(i+1)
			if (!ptr.hasOwnProperty(substr)) { return false } 
			ptr = ptr[substr]
		}
        
		return ptr.hasOwnProperty(WORD_MARKER) ? true : false 
        
	}

	_isSubstr(ptr, word) {
		/*
		@ param a query string
		@ returns 
			  -1 if this is not a substring of anything, or the index
			  of the last point in the string (or 19 if it is a long string)
			  if the word is a substring of something

			  It also mutates the pointer given to it

		*/
		var i = 0
		while (i < word.length) {
			let ch = word.charAt(i)
			if (ptr.hasOwnProperty(ch)) {
				ptr = ptr[ch]
			}  else {
				return [ptr, -1]
			}
			if (i === MAX_LEN) { break }
			i++
			// console.log(ptr)
		}
		return [ptr, i]
	}

	_buildWords(prefix, tree) {
		/*
		builds words from a starting prefix
		*/
		var lst = []
		appendingDFS(prefix, tree, lst)
		return lst

	}

	autocomplete(prefix) {
		/*
		Finds words that can result from a given prefix
		*/
		let ptr = {...this._trie}
		let tup = this._isSubstr(ptr, prefix)
		let i = tup[1]
		ptr = tup[0]

		if( i < 0) {
			return []
		}
		return this._buildWords(prefix, ptr)
	}
}

export default Trie