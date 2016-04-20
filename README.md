## GenStringsPy


#### About project

This simple script was created while I was working on a Swift iPad application.  
Since we required the functionality of switching the language at runtime, we have created a simple String extension:  

~~~Swift
extension String {
    func localize() -> String {
        var path = NSBundle.mainBundle().pathForResource(CURRENT_LANGUAGE, ofType: "lproj")
        if(path == nil) {
            path = NSBundle.mainBundle().pathForResource("Base", ofType: "lproj")
        }
        let bundle = NSBundle(path: path!)
        
        return NSLocalizedString(self, tableName: nil, bundle: bundle!, value: "", comment: "")
    }
}
~~~

And then use it in the project like this:   

`closeButton.setTitle("Cancel".localize(), forState: .Normal)`

And well, I do prefer using such construct than `NSLocalizedString("key", comment: "comment")` 😉

The problem with such approach is that XCode does not work with such solution and won't export the `Localized.strings` file.

But having to export all the strings manually would be really cumbersome task.  

So, that's how this script was born 😄 

#### How to use it?

1. Clone the repo or copy the script somewhere to your computer :) 
2. `python genstrings.py /path/to/your/ios/project/root`
3. Copy output `Localized.strings` and send it to your translators to fill the placeholders :) 

#### Limitations / TODO
* Requires specific localization construct : `"Desired key".localize()`
* Cannot traverse folder structure

I'll try to fix them in my spare time, but if you find the solution earlier on, send a pull request :) 

If you have any troubles, file an issue.

Happy using ;) 
