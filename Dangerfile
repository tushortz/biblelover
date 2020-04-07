# Use the VS Code Spell-checker word ignore list
require 'json'

avoid_exact_words = [
  { word: 'Github', reason: "Please use GitHub, capital 'H'" },
  { word: 'Cocoapods', reason: "Please use CocoaPods, capital 'P'" },
  { word: 'Javascript', reason: "Please use JavaScript, capital 'S'" },
  { word: 'Typescript', reason: "Please use TypeScript, capital 'S'" },
  { word: 'Fastlane', reason: "Please use fastlane, lowercase 'f'" },
  { word: 'localhost:4000', reason: 'You may have left an internal link in the markdown' },
  { word: '[]: ???', reason: 'You\'ve missed a link' },
  { word: '[TODO]', reason: 'You may have missed a TODO here' },
  { word: 'react native', reason: 'Please use React Native with capitals' }
]

active_files = (git.modified_files + git.added_files).uniq
markdowns = active_files
  .select { |file| file.start_with? '_posts/' }
  .select { |file| file.end_with?('.md', '.markdown') }

# This could do with some code golfing sometime
markdowns.each do |filename|
  file = File.read(filename)
  lines = file.lines
  fail("Please add a <!-- more --> tag where you'd like this post to break for post preview", file: filename) unless file.include?("<!-- more -->")
  lines.each do |l|
    avoid_exact_words.each do |avoid|
      line = lines.index line
      warn(avoid[:reason], file: filename, line: line) if l.include? avoid[:word]
    end
  end
end

# Just to let people know
warn("PR is classed as Work in Progress") if github.pr_title.include? "[WIP]"

if github.pr_title.length < 5
    fail "Please provide a descriptive title in the Pull Request"
  end
  
# # Ensure a clean commits history
# if git.commits.any? { |c| c.message =~ /^Merge branch '#{github.branch_for_base}'/ }
#   fail('Please rebase to get rid of the merge commits in this PR')
# end

code_style_validation.check validator: 'pylint', file_extensions: ['.py'], ignore_file_patterns: ['**/migrations/*.py']