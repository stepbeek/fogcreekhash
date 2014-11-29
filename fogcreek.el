;; Solution to the fogcreek dehashing problem


(setq key "acdegilmnoprstuw")
(setq initial 7)


(defun revstr (str)
  "Reverse the str where str is a string"
  (apply #'string 
         (reverse 
          (string-to-list str))))

(defun dehash (h)
  "Dehash the fogcreek problem"
  (if (eq h initial) ""
    (let ((indx (% h 37)))
      (concat (substring key indx (+ indx 1)) 
              (dehash (/ (- h indx) 37)
                      )))))

(revstr (dehash 945924806726376))
